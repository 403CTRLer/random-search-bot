# Random Search Bot

The Random Search Bot is a Python script that opens Microsoft Edge on Windows or a web browser on Android devices and performs a specified number of random searches using Bing. This script is a fun and interactive way to simulate search activity and explore the web with randomized queries and basically works with Microsoft Reward Acitvities.

## Prerequisites

- Python 3.x
- Microsoft Edge browser (for Windows)
- Android device with a Edge browser (for Android)
- [EdgeDriver for Windows](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (corresponding to installed Edge version)
- [ADB Tools](https://developer.android.com/studio/releases/platform-tools) for Windows

## Getting Started

1. Clone the repository or download the script files.

   ```bash
   git clone https://github.com/your-username/random-search-bot.git
   ```

2. Ensure that you have the required environment set up according to your operating system.

   - For Windows:
     - Install Microsoft Edge on your system.
     - Download the appropriate version of EdgeDriver based on your installed Edge version and place it in the repository folder.

   - For Android:
     - Ensure you have a Edge browser installed on your Android device.
     - Install ADB Tools on your computer.

## Usage

### For Windows

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the script by executing the following command:

   ```bash
   python search_windows.py
   ```

3. Microsoft Edge will launch, and the script will prompt you to enter the number of searches to perform. If no input is provided, it will default to 30 searches.

4. The script will generate random search queries and open Bing search results for each query in separate tabs in Microsoft Edge.

5. Enjoy watching the random search activity in the browser!

### For Android

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the script by executing the following command:

   ```bash
   python search_android.py
   ```

3. The script will prompt you to enter the number of searches to perform. If no input is provided, it will default to 20 searches.

4. The script will generate random search queries and open Bing search results for each query in the web browser on your Android device.

5. Enjoy watching the random search activity in the mobile browser!

## Customization

You can customize the behavior of the Random Search Bot by modifying the following variables in the script:

- For Windows:
  - `EDGE_PATH`: The file path to the Microsoft Edge executable. Update this variable if Edge is installed in a different location on your system.

- For both:
  - `length`: The length of the random search query. By default, it is set to 10 characters.
  - `num_searches`: The number of searches to perform. You can modify this variable directly in the script or provide the value when prompted during runtime.
  - `generate_random_query`: Modify this function to get desired search queries.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Random Search Bot script is inspired by the idea of simulating search activity and exploring the web in a randomized manner.
- Special thanks to the developers of Microsoft Edge, Bing, EdgeDriver, ADB Tools, and the Python community for providing the tools, services, and libraries to make this project possible.
- Thanks to boredem and laziness experienced while engaing with activities on the Microsoft Rewards page, resulting in the birth of this script.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## Disclaimer

Please use this script responsibly and consider the legal and ethical implications of automated search activity. The Random Search Bot is intended for educational and entertainment purposes only. The authors and contributors of this project are not responsible for any misuse or unauthorized activities conducted using this script.

Enjoy exploring the web with the Random Search Bot! Happy searching!