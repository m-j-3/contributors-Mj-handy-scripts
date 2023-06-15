#include <iostream>
#include <string>
#include <filesystem>

int main(int argc, char* argv[]) {
    std::string folderName = "New Folder";
    int folderCount = 0;

    while (std::filesystem::exists(folderName)) {
        ++folderCount;
        folderName = "New Folder (" + std::to_string(folderCount) + ")";
    }

    std::filesystem::create_directory(folderName);

    for (int i = 1; i < argc; ++i) {
        std::filesystem::path itemPath = argv[i];
        std::filesystem::path destinationPath = folderName + "\\" + itemPath.filename().string();
        if (itemPath != destinationPath) {
            std::filesystem::rename(itemPath, destinationPath);
        }
    }

    return 0;
}


// i wrote this cuz it annoyed me that you could send things to zipped files but not send things to normal files so if you put the new folder exe in the send to folder under microsoft under windows (i think thats the path) then youll have the ability to do this from the send to menu when you right click while dealing with files :)