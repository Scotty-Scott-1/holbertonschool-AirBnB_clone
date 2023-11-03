import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()
        self.console = HBNBCommand()
        self.obj = BaseModel()
        self.obj.save()

    def tearDown(self):
        self.patcher.stop()

    def test_do_create_with_valid_class(self):
        class_name = "BaseModel"
        cmd_input = f"create {class_name}\n"
        expected_output = f"{self.cmd.models['BaseModel'].id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create BaseModel")
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_create_with_valid_class(self):
        class_name = "BaseModel"
        cmd_input = f"create {class_name}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create BaseModel")
        actual_output = self.mock_stdout.getvalue().strip()
        self.assertIsNotNone(actual_output)
        self.assertRegex(actual_output, r'^[0-9a-f-]+$')

    def test_do_create_with_no_class_name(self):
        cmd_input = "create\n"
        expected_output = "** class name missing **\n"

        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("create")

        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_show_with_valid_instance(self):
        # Create a BaseModel instance
        base_model = BaseModel()
        instance_id = base_model.id
        class_name = "BaseModel"
        cmd_input = f"show {class_name} {instance_id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"show {class_name} {instance_id}")
        expected_output = str(base_model) + "\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_show_with_nonexistent_instance(self):
        cmd_input = "show BaseModel 12345\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("show BaseModel 12345")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_destroy_with_valid_instance(self):
        # Create a BaseModel instance
        base_model = BaseModel()
        instance_id = base_model.id
        class_name = "BaseModel"
        cmd_input = f"destroy {class_name} {instance_id}\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd(f"destroy {class_name} {instance_id}")
        self.assertIsNone(storage.all().get(f"{class_name}.{instance_id}"))

    def test_do_destroy_with_nonexistent_instance(self):
        cmd_input = "destroy BaseModel 12345\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("destroy BaseModel 12345")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_all_with_class_argument(self):
        # Create some instances of BaseModel and User
        base_model_1 = BaseModel()
        user_1 = User()
        cmd_input = "all BaseModel\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("all BaseModel")
        actual_output = self.mock_stdout.getvalue()
        self.assertIn(str(base_model_1), actual_output)
        self.assertNotIn(str(user_1), actual_output)

    def test_do_all_with_empty_argument(self):
        # Create some instances of BaseModel
        base_model_1 = BaseModel()
        cmd_input = "all\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("all")
        actual_output = self.mock_stdout.getvalue()
        self.assertIn(str(base_model_1), actual_output)

    def test_update_valid_attribute(self):
        instance_id = self.obj.id
        with patch('builtins.input', side_effect=['update BaseModel', instance_id, 'non_existent_attribute', 'John']):
            self.cmd.onecmd("update BaseModel {} non_existent_attribute 'John'".format(instance_id))
        expected_output = "** value missing **\n"  # Output message in case 'non_existent_attribute' does not exist
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_do_update_with_nonexistent_instance(self):
        cmd_input = "update BaseModel 12345 name \"UpdatedName\"\n"
        with patch('builtins.input', side_effect=cmd_input):
            self.cmd.onecmd("update BaseModel 12345 name \"UpdatedName\"")
        expected_output = "** no instance found **\n"
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
