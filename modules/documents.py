import random

ID_KEY = "id"
CLASSIFICATIONS_KEY = "classifications_dpf"
AWESOME_NUMBER_KEY = "awesome_number"
AWESOME_STRING_KEY = "awesome_string"
AWESOME_MULTI_FIELD_KEY = "awesome_multi_field"
CLASSES = [
    "first_classifier:class_one",
    "first_classifier:class_two",
    "first_classifier:class_three",
    "first_classifier:class_four",
    "second_classifier:class_one",
    "second_classifier:class_two"
]
NUMBER_OF_CLASSES = len(CLASSES)


def create_doc(j):
    random_three_classes = random.sample(CLASSES, 3)
    return {
        ID_KEY: "document.{0}".format(str(j)),
        CLASSIFICATIONS_KEY: list(
            ("{0}|{1}".format(str(j), str(round(random.uniform(0, 1), 2))) for j in random_three_classes)),
        AWESOME_MULTI_FIELD_KEY: random_three_classes,
        AWESOME_STRING_KEY: CLASSES[random.randint(0, NUMBER_OF_CLASSES - 1)],
        AWESOME_NUMBER_KEY: round(random.uniform(0, 1), 2)
    }
