# label-bob
label-bob is a fast tool to annotate youtube videos for [mmaction 2](https://github.com/open-mmlab/mmaction2). This tool downloads youtube clips, helps label the individual frames and extracts them to be ready for training compatible with MMCV formatting.

![](https://github.com/Oh-hi-marx/label-bob/blob/master/readme/ui.png)

## Installation
After cloning the repository and going inside the repository root, install all the pre-requisite libraries by running:
```
pip install -r requirements.txt
```


## Tutorial
### Creating a link collection
Before labelling, the urls for the youtube clips need to be stored in a text file inside the root directory of the repository. Each link needs to be on a different line. An example is shown below:

![](https://github.com/Oh-hi-marx/label-bob/blob/master/readme/link-collection.png)

### Running auto
To run the all the tools one after another, do the following on bash:
```
bash auto.sh
```
If on a windows operating system, you may run the following instead:
```
python auto-run.py
```

Follow the step by step guide on each tool to follow along on the next steps. **Note:** You do not need to run the commands again as ```auto.sh``` or ```auto-run.py``` does it for you.

### Downloading the clips

Run the following to start downloading the clips mentioned in the link collection:
```
python downloadFromTxt.py
```
After running the script it will ask for the text file that is in the root directory of the repo that has all the links in it. Input the text file name (without the extention). After input, the tool will start downloading the youtube clips into ```/downloads``` folder.

### Extracting the frames
To run this tool separately, run:
```
python ExtractFrames.py
```
This will extract the individual frames for each clip stored in ```/downloads``` and put them into the ```/inputs``` folder.

### Labelling

To start labelling, run:
```
python edit.py
```

On the label screen, use ```A``` and ```D``` to go through the frames. To mark the start of a clip, use ```S``` and then enter a number for the class ID. Use ```Delete``` to delete the class number. To mark the end of a clip, press ```W```. The frame number, classes, and the current labels will be shown on the terminal. To remove the last label, press ```Z```.

After labelling is complete for the current video, press ```ESC``` to finish. The labels are stored in the following format inside the annotations file:
```
startFrame endFrame classNumber
```
The annotation file with the labels will then be stored inside ```/segmentLabels```.

### Export to MMCV raw frames format

To export frames into a label.txt file, compatible with the MMCV mmaction2 rawframes format, run:
```
python segment.py
```
A ```/outputs``` folder and an associated ```/outputs/labels.txt``` file  will be generated. These can directly be placed into a mmaction dataset folder for training.

## Citation
If this tool was useful, please consider citing:
```
@misc{2022label-bob,
    title={Youtube Download and Labelling Tool For MMAction 2},
    author={oh-hi-marx},
    howpublished = {\url{https://github.com/Oh-hi-marx/label-bob}},
    year={2022}
}
```

## License
This project is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
