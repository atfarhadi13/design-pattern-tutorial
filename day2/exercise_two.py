from typing import Protocol, Any
import json


class Serializer(Protocol):
    def serialize(self, data: Any) -> str:
        ...


class JsonSerializer:
    def serialize(self, data: Any) -> str:
        """Serialize Python data to JSON string."""
        return json.dumps(data, ensure_ascii=False)


class XmlSerializer:
    def serialize(self, data: dict) -> str:
        """
        Fake XML serializer just for practice.
        Very simplified: only handles flat dicts.
        """
        items = []
        for key, value in data.items():
            items.append(f"<{key}>{value}</{key}>")
        body = "".join(items)
        return f"<root>{body}</root>"


# --- Demo usage ---
if __name__ == "__main__":
    payload = {
        "id": 123,
        "user": "Amin",
        "status": "confirmed",
    }

    json_serializer: Serializer = JsonSerializer()
    xml_serializer: Serializer = XmlSerializer()

    print("JSON:")
    print(json_serializer.serialize(payload))

    print("\nXML:")
    print(xml_serializer.serialize(payload))
