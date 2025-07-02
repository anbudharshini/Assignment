import os

class DBPropertyUtil:
    @staticmethod
    def get_connection_properties(file_path=None):
        if not file_path:
            # Automatically resolve full path
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_path, "util", "config.txt")
        try:
            with open(file_path, 'r') as file:
                properties = {}
                for line in file:
                    if '=' in line:
                        key, value = line.strip().split('=')
                        properties[key.strip()] = value.strip()
                return properties
        except Exception as e:
            print(f"Error reading property file: {e}")
            return None
