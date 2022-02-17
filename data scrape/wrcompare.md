SELECT * 

FROM "akulkarnii/ProgenyCompacter"."cfb_2019_wr.xlsx - Sheet1" as cfb join "akulkarnii/ProgenyCompacter"."nfl_2021_wr.xlsx - Sheet1" as nfl on cfb.Player = nfl.Player

ORDER BY nfl.points;