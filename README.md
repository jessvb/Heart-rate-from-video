# Heart-rate-from-video
*Detect heart rate from local video recordings!* This repository was forked from [habom2310/Heart-rate-measurement-using-camera](https://github.com/habom2310/Heart-rate-measurement-using-camera).

## Usage
1. Clone the project locally
2. In the project root, create a `recordings` folder and an `output` folder
3. Place a `.avi` recording (that you'd like to use heart rate detection on) into the `recordings` directory
4. Open the `heart-rate-post-process.py` file and change the `input_video` variable contents to be the name of your `.avi` file
5. In a terminal, `cd` into the project root
6. Run `pip install -r requirements.txt`
7. Run `python heart-rate-post-process.py` to detect heart rate from your video
8. View the output `.csv` file with the recognized heart rate in the `output` directory