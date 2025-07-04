from django.conf import settings
import base64
import os


def is_valid_header(request):
    validation_value = request.headers.get("`Validation`")

    print(f"Validation header value: {validation_value}")  # Debugging output
    return str(validation_value) == "335792"


# "get_sent_build_qsts" router help functions
def create_sent_build_item(question, possible_answers):
    return {"question": question, "possibleAnswers": possible_answers}


# "get_unseen_qsts" router help functions
def encode_image_to_base64(image_path: str):
    with open(os.path.join(settings.BASE_DIR, image_path), "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
