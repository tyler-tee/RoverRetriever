import requests


class Retriever:

    def __init__(self):
        self.base_url = 'https://dog.ceo/api'

        self.client = requests.session()

    ERROR_DICT = {
                    404: "Requested resource could not be found.",
                    500: "Unexpected error - If the problem persists, please contact support."
                                }

    def _make_request(self, method, resource, **kwargs):
        url = f'{self.base_url}/{resource}'
        response = self.client.request(method, url, **kwargs)

        # Check for a successful response
        if response.status_code == 200:
            return {'success': True, 'data': response.json()}

        error_details = {
            'success': False,
            'status_code': response.status_code,
            'reason': response.reason,
            'message': self.ERROR_DICT.get(response.status_code,
                                           "An error occurred with your request."),
            'details': response.text
        }

        return error_details

    def get_breeds(self) -> dict:
        """
        Returns a List of all available dog breeds.

        Returns:
            dict: {
                'success': bool
                'data': {
                    'breeds': [breeds_list]
                }
            }
        """

        response = self._make_request('GET', 'breeds/list/all')

        return response

    def get_all_sub_breeds(self, breed: str) -> dict:
        """
        Returns array of possible sub breeds associated with specified breed.

        Returns:
            dict: {
                'success': bool,
                'data': [sub_breeds_lst]
            }
        """

        resource = f'/breed/{breed}/list'
        response = self._make_request('GET', resource)

        return response

    def get_random_image(self) -> dict:
        """
        Returns a single random image from the 'All Dogs' collection.

        Returns:
            dict: {
                'success': bool
                'data': str
                }
        """

        response = self._make_request('GET', 'breeds/image/random')

        return response

    def get_images_by_breed(self, breed: str) -> dict:
        """
        Returns an array of all images from a specified breed.

        Args:
            breed (str): Breed name (obtained via get_breeds())

        Returns:
            dict: {
                'success': bool,
                'data': [image_lst]
                }
        """

        resource = f'/breed/{breed}/images'
        response = self._make_request('GET', resource)

        return response
