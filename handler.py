from typing import Dict, List, Any

from facexformer_pipeline import FacexformerPipeline
from image_input_handler import UniversalImageInputHandler


class EndpointHandler():
    def __init__(self, path=""):
        # Preload all the elements you are going to need at inference.
        self.model = FacexformerPipeline(debug=True, tasks=['attributes', 'age_gender_race'])

    def __call__(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
       data args:
            inputs (:obj: `str` | `PIL.Image` | `np.array`)
            kwargs
      Return:
            A :obj:`list` | `dict`: will be serialized and returned
        """
        # Put your code for reading an image 
        image_path = data['inputs']
        uih = UniversalImageInputHandler(image_path)
        img = uih.img

        # Run the model on an image
        results = self.model.run_model(img)
        return results
