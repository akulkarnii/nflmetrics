SELECT player, 0.3 * diffrat + 0.25 * difftda + 0.2 * diffypt + 0.15 * diffcmp + 0.1 * "int" as cbrank

FROM (

SELECT player, "int", -1 * ("Cmp%" - avgCmp) as diffCmp, -1 * ("Yds/Tgt" - avgYPT) as diffYpt, -1 * (TD - avgTDA) as diffTda, -1 * (Rat - avgRat) as diffRat

FROM "akulkarnii/ProgenyCompacter"."nfl_2021_cbs.xlsx - Sheet1"

CROSS JOIN (

  SELECT avg("Cmp%") as avgCmp

  FROM "akulkarnii/ProgenyCompacter"."nfl_2021_cbs.xlsx - Sheet1"

) as t2

CROSS JOIN (

  SELECT avg("Yds/Tgt") as avgYPT

  FROM "akulkarnii/ProgenyCompacter"."nfl_2021_cbs.xlsx - Sheet1"

) as t3

CROSS JOIN (

  SELECT avg(TD) as avgTDA

  FROM "akulkarnii/ProgenyCompacter"."nfl_2021_cbs.xlsx - Sheet1"

) as t4

CROSS JOIN (

  SELECT avg(Rat) as avgRAT

  FROM "akulkarnii/ProgenyCompacter"."nfl_2021_cbs.xlsx - Sheet1"

) as t5

ORDER BY diffRat desc

) as CBModel

ORDER BY cbrank desc;