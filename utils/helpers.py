import base64

def encode_file_to_base64(file_path):
    """Encodes a file to a base64 string."""
    try:
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read()).decode("utf-8")
        return encoded_string
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"Error encoding file to base64: {e}")
        return None