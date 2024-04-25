#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <filesystem>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;
namespace fs = filesystem;

// Main Class of the Application
class generalItem {

private:

    // Subject indexing parameters

    string id;
    string itemCity;
    string itemQuality;

    // Main item parameters
    unsigned long sellPriceMin; string sellPriceMinUpdateDate;

    unsigned long sellPriceMax; string sellPriceMaxUpdateDate;

    unsigned long buyPriceMin; string buyPriceMinUpdateDate;

    unsigned long buyPriceMax; string buyPriceMaxUpdateDate;

public:

    // Construct Class
    generalItem(
    
    string item_id, 
    string city, 
    string quality,
    
    unsigned long sell_price_min, string sell_price_min_date,

    unsigned long sell_price_max, string sell_price_max_date,

    unsigned long buy_price_min, string buy_price_min_date,

    unsigned long buy_price_max, string buy_price_max_date
    
    )
    
    {
        // Passing data to main class variables

        // Identifiers
        id = item_id; // Name of the item
        itemCity = city; // City of the item
        itemQuality = quality; // Quality of the item

        // Prices of Minimum
        sellPriceMin = sell_price_min; // Minimum sell price of the item
        sellPriceMinUpdateDate = sell_price_min_date; // Minimum sell update date of the item
        
        sellPriceMax = sell_price_max; // Maximum sell price of the item
        sellPriceMaxUpdateDate = sell_price_max_date; // Maximum sell update date of the item
        
        // Prices of Maximum
        buyPriceMin = buy_price_min; // Minimum buy price of the item
        buyPriceMinUpdateDate = buy_price_min_date; // Minimum buy update date of the item

        buyPriceMax = buy_price_max; // Maximum buy price of the item
        buyPriceMaxUpdateDate = buy_price_max_date; // Maximum buy update date of the item
    }


};


string readJsonFile(const fs::path& filePath) {
    ifstream file(filePath);
    if (!file.is_open()) {
        throw runtime_error("Не удалось открыть файл " + filePath.string());
    }
    return string((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
}




int main(){

    const std::string mainFolderOfJsonFile = "Last_JSON_File/";

    if (!fs::is_directory(mainFolderOfJsonFile)) {
        cerr << "The specified path is not a folder" << endl;
        return 1;
    }

    try {
        for (const auto& entry : fs::directory_iterator(mainFolderOfJsonFile)) {
            if (entry.is_regular_file() && entry.path().extension() == ".json") {
                string fileName = entry.path().filename().string();

                string jsonDataString = readJsonFile(entry.path());
                json jsonData = json::parse(jsonDataString);

                //Workspace directory

                cout << "yes";


                
            }
        }
    } catch (const exception& e) {
        cerr << "Ошибка: " << e.what() << endl;
        return 1;
    }


    return 0;
}
