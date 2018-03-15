import WebScrapper as WS
import TrieOOP
import dataWriter as DW

WS.mainStarter('radiohead', *WS.getAlbumSongs('radiohead', 'amnesiac'))
data1 = WS.tree.getData(WS.tree)
data2 = WS.tree.getAll(data1)
DW.xlsxWriter(data1, data2, "amnesiac")
