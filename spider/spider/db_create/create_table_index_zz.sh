



sql="use stock;
      create table IF NOT EXISTS index_zz
      (
        indexCompliance String,
        indexComplianceEn String,
        ifTracked String,
        ifTrackedEn String,
        indexSeries String,
        indexSeriesEn String,
        key String,
        indexCode String,
        indexName String,
        indexNameEn String,
        consNumber String,
        latestClose String,
        monthlyReturn String,
        indexType String,
        assetsClassify String,
        assetsClassifyEn String,
        hotSpot String,
        hotSpotEn String,
        region String,
        regionEn String,
        currency String,
        currencyEn String,
        ifCustomized String,
        ifCustomizedEn String,
        indexClassify String,
        indexClassifyEn String,
        ifWeightCapped String,
        ifWeightCappedEn String,
        publishDate String,
        ifProtect String,
        protectStartDate String,
        protectEndDate String,
        ifTopDing String,
        
        dt String
      ) ENGINE = MergeTree
        PARTITION BY dt order by dt;
    "

clickhouse-client \
  --host localhost \
  --port 9000 \
  --user default \
  --password click!@#123 \
  --multiquery -q  "${sql}"


