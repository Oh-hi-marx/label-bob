# label-bob
label-bob is a fast tool to annotate youtube videos for [mmaction 2](https://github.com/open-mmlab/mmaction2). This tool downloads youtube clips, helps label the individual frames and extracts them to be ready for training.

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

### Running the script
To run the tool, do the following on bash:
```
bash auto.sh
```
If on a windows operating system, you may run the following instead:
```
python auto-run.py
```

After running the script it will ask for the text file that is in the root directory of the repo that has all the links in it. Input the text file name (without the extention). After input, the tool will start downloading the youtube clips into ```/downloads``` folder, and then extract the individual frames for youtube clip into ```/outputs``` folder. The labels are stored inside ```/segmentLabels``` after labelling has been completed.

### Labelling
On the label screen, use ```A``` and ```D``` to go through the frames. To mark the start of a clip, use ```S``` and then enter a number for the class ID. To mark the end of a clip, press ```W```. The frame number, classes, and the current labels will be shown on the terminal. To remove the last label, press ```Z```.



After labelling is complete for the current video, press ```ESC``` to finish. The labels are stored in the following format inside the annotations file:
```
startFrame endFrame classNumber
```
The annotation file with the labels will then be stored inside ```/segmentLabels```.

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
