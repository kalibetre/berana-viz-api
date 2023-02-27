from django.core.exceptions import ValidationError


def nodes_validator(value):
    """
    A validator that checks wether the `nodes` attribute of a Document is an
    array/list of integers

    Args:
        value (Document): parsed document form the serializer

    Raises:
        ValidationError: if document does not have a nodes attribute
        ValidationError: if nodes attribute is not an array of numbers
    """
    if 'nodes' not in value:
        raise ValidationError(
            'Document Content must have a nodes attribute with a array '
            'of numbers')
    else:
        numbers = value.get("nodes", None)
        if (not isinstance(numbers, list)
                or any([not isinstance(n, int) for n in numbers])):
            raise ValidationError(
                'The nodes attribute must be an array of numbers')
