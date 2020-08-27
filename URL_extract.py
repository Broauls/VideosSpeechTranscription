# outfile = open("URL_Vimeo.txt", "w")
outfile = open("URL_Youtube.txt", "w")


# with open("../dataset/COVID-19_Datasets_OnlineVideos/covid-19_VimeoDataset.txt", "r", encoding='utf-8') as dataset:
with open("../dataset/COVID-19_Datasets_OnlineVideos/covid-19_YoutubeDataset.txt", "r", encoding='utf-8') as dataset:

    for line in dataset:
        if line[1:6] == "TITLE":
            if (line.lower().find("stock footage") != -1) or (line.lower().find("stock video footage") != -1):
                isAStockFootage = True
            else:
                isAStockFootage = False

        if line[1:4] == "URL" and isAStockFootage == False:
            endline = line[1:].find("<")
            tempURL = line[6:endline] + "\n" #keep the url , write it after looking at the description

        if line[1:12] == "DESCRIPTION" and isAStockFootage == False:
            if (line.lower().find("stock footage") == -1) or (line.lower().find("stock video footage") == -1):
                outfile.write(tempURL)