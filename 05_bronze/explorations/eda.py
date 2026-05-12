# Databricks notebook source
# MAGIC %md
# MAGIC # EDA on supply chain

# COMMAND ----------


VOLUME_PATH = "/Volumes/supply_chain_demo/default/raw"

spark.sql(f"LIST '{VOLUME_PATH}'").display()

# COMMAND ----------

spark.sql(f"LIST '{VOLUME_PATH}/data'").display()
