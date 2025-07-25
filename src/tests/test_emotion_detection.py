from src.emotion_detection import emotion_detection
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_get_emotion_eval(self):
        tests = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for key, val in tests.items():
            result = emotion_detection.get_emotion_eval(key)['dominant_emotion']
            self.assertEqual(result, val)


if __name__ == '__main__':
    unittest.main()
