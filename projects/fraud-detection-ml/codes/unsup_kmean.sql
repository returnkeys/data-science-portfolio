CREATE OR REPLACE MODEL
  finance.model_unsupervised OPTIONS(model_type='kmeans', num_clusters=5) AS
SELECT
  amount, oldbalanceOrig, newbalanceOrig, oldbalanceDest, newbalanceDest, type, origzeroFlag, destzeroFlag, amountError
  FROM
  `finance.fraud_data_model`