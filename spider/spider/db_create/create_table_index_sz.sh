



sql="use stock;
          create table IF NOT EXISTS index_sz
          (
          handbookUrl String               ,
nIndexFullNameEn String          ,
nIndexNameEn String              ,
tIndexCode String                ,
nIndexCode String                ,
indexReleaseChannel String      ,
indexCode String                 ,
introEn String                   ,
indexFullName String             ,
nIndexFullName String            ,
totalReturnIntro String          ,
tIndexNameEn String              ,
indexFullNameEn String           ,
isNetLncomeIndex String         ,
intro String                     ,
tIndexFullName String            ,
indexBaseDay String              ,
ifIndexCode String               ,
numOfStockes String             ,
netReturnIntroEn String          ,
indexBasePoint String           ,
indicsSeqDescEn String           ,
indexName String                 ,
netReturnIntro String            ,
isPriceIndex String             ,
updateTime String                ,
indicsSeqDesc String             ,
indexDataSourceType String      ,
launchDay String                 ,
methodologyNameEn String         ,
methodologyName String           ,
tIndexFullNameEn String          ,
handbookEnUrl String             ,
indicsSeq String                ,
nIndexName String                ,
indexNameEn String               ,
totalReturnIntroEn String        ,
tIndexName String                ,
isTotalReturnIndex String       ,
            dt String
          ) ENGINE = MergeTree
          PARTITION BY dt order by dt;
          "

clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#\
  --multiquery -q  "${sql}"


# 按分区删除，注意是单引号
delete from index_sz where dt = '2023-12-12';