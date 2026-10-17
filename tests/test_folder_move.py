from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import _folder_move as organizer


class FolderMoveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def put(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_archives_keep_active_files_and_associated_data(self):
        self.put("ABC479A.py", "active")
        self.put("PAST04/PAST04A.py", "past")
        self.put("ADT/ADT_20231018_2A.py", "adt")
        self.put("yuki/yuki_0247.py", "yuki")
        self.put("yuki/yuki_0148_X.txt", "data")
        self.put("ABC/ABC168/in/sample.txt", "input")
        moves = organizer.plan_moves(self.root, include_root=False)
        self.assertEqual(len(moves), 4)
        organizer.apply_moves(self.root, moves)
        for relative, text in {
            "ABC479A.py": "active", "PAST/PAST004/PAST004A.py": "past",
            "ADT/20231018/ADT_20231018_2A.py": "adt", "yuki/02xx/yuki_0247.py": "yuki",
            "yuki/01xx/yuki_0148_X.txt": "data", "ABC/ABC168/in/sample.txt": "input",
        }.items():
            self.assertEqual((self.root / relative).read_text(encoding="utf-8"), text)
        self.assertFalse((self.root / "PAST04").exists())
        self.assertEqual(organizer.plan_moves(self.root, include_root=False), [])

    def test_collisions_keep_all_versions_and_reserved_names(self):
        self.put("ABC/ABC010/ABC010D.py", "original")
        self.put("ABC/ABC010/ABC010D_alt2.py", "existing alternate")
        self.put("ABC010D.py", "new root version")
        self.put("ABC/ABC010/ABC010/ABC010D.py", "nested version")
        moves = organizer.plan_moves(self.root)
        organizer.apply_moves(self.root, moves)
        files = self.root / "ABC/ABC010"
        self.assertEqual((files / "ABC010D_alt3.py").read_text(), "new root version")
        self.assertEqual((files / "ABC010D_alt4.py").read_text(), "nested version")
        self.assertEqual((files / "ABC010D.py").read_text(), "original")
        self.assertEqual((files / "ABC010D_alt2.py").read_text(), "existing alternate")
        self.assertEqual(organizer.plan_moves(self.root), [])

    def test_target_created_after_preview_aborts_before_any_move(self):
        first = self.put("ARC232A.py", "first")
        second = self.put("AGC079A.py", "second")
        moves = organizer.plan_moves(self.root)
        self.put("ARC/ARC232/ARC232A.py", "created later")
        with self.assertRaises(FileExistsError):
            organizer.apply_moves(self.root, moves)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

    def test_cli_defaults_to_preview_and_uses_script_directory(self):
        script = self.root / "_folder_move.py"
        shutil.copyfile(organizer.__file__, script)
        source = self.put("AGC079A.py", "solution")
        command = [sys.executable, "-X", "utf8", str(script)]
        subprocess.run(command, cwd=self.root.parent, check=True, capture_output=True)
        self.assertTrue(source.exists())
        subprocess.run(command + ["--apply"], cwd=self.root.parent, check=True, capture_output=True)
        self.assertEqual((self.root / "AGC/AGC079/AGC079A.py").read_text(), "solution")


if __name__ == "__main__":
    unittest.main()
