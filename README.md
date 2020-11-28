# Heart-rate-from-video
*Detect heart rate from local video recordings!* This repository was forked from [habom2310/Heart-rate-measurement-using-camera](https://github.com/habom2310/Heart-rate-measurement-using-camera).

## Usage
1. Clone the project locally
2. In the project root, create a `recordings` folder and an `output` folder
3. Place `.avi`/`.mp4` recording(s) (that you'd like to use heart rate detection on) into the `recordings` directory
4. In a terminal, `cd` into the project root
5. Run `pip install -r requirements.txt`
6. Run `python heart-rate-post-process.py` to detect heart rate from your video(s)
7. View the output `.csv` file with the recognized heart rate in the `output` directory