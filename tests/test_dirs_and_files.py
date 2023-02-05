from src.GetData import GetData


def test_list_dir(base_url, token):
    auth = GetData(base_url, token)
    req = auth.get_dir()
    data = auth.list_dir()
    auth.print_list(data)
    assert req.status_code == 200
    assert auth.validation_json_schema(req, auth.SCHEMA_DIR) is True, "schema is not valid"


def test_list_folder(base_url, token):
    auth = GetData(base_url, token)
    req = auth.get_file()
    data = auth.list_file()
    auth.print_list(data)
    assert req.status_code == 200
    assert auth.validation_json_schema(req, auth.SCHEMA_FILE) is True, "schema is not valid"
