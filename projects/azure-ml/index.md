# ☁️ Azure Machine Learning — Practical Work

I built, ran, and iterated complete ML workflows on Microsoft Azure using **Designer** and the **SDK v2**.  
The focus is enterprise-style delivery: reproducible pipelines, model registry, deployment to online endpoints, and light monitoring.

---

## 🔧 Environment & Resources

I provisioned a dedicated **resource group** and **Azure ML workspace**, backed by blob storage and a CPU cluster for training/inference.  
Workloads were authored as Designer graphs (for clarity) and as SDK jobs (for automation & CI readiness).

**Key factors**
- Workspace, compute cluster, and datastores configured for repeatable runs  
- Data registered as **Data assets** (versioned URIs/folders)  
- Jobs tracked in **Experiments**; models promoted to the **Model Registry**  
- Optional online endpoints created for real-time scoring

---

## 📚 Datasets

I used three tabular datasets to exercise supervised and unsupervised workflows.  
Each dataset was registered as a **Data asset** and referenced across experiments.

**Key factors**
- **Automobile price** (regression): numeric `price` target; mixed numeric/categorical features  
- **Diabetes** (classification): binary outcome; standard medical predictors  
- **Penguins** (clustering): unlabeled data to validate segmentation with K-Means  
- Stored in `workspaceblobstore` under organized paths for pipeline reuse

---

## 1) Regression — Automobile Price Prediction

This workflow predicts vehicle price and publishes a scored output suitable for a simple REST endpoint.  
The Designer graph captures the full lineage from ingestion to evaluation and web-service I/O.

**Key factors**
- **Prep:** Convert/ingest → Select Columns → Transform/Normalize (handled outliers/scales)  
- **Modeling:** tuned tree-based regressor as a strong baseline; AutoML used to cross-check  
- **Evaluation:** RMSE/MAE/R² logged per run; comparisons drove feature selection refinements  
- **Deployment:** Web Service Input/Output blocks integrated; endpoint validated with sample payloads  
- **Ops:** artifacts saved with run IDs; best model version registered for promotion

---

## 2) Classification — Diabetes Risk

This pipeline classifies risk and demonstrates threshold tuning for business-friendly precision/recall tradeoffs.  
I iterated across several runs (including some failed→fixed) to document debugging and reproducibility.

**Key factors**
- **Prep:** Select Columns → Clean Missing → Normalize; categorical handling kept explicit  
- **Modeling:** logistic/gradient-boosting candidates; threshold tuning to optimize **F1/AUC**  
- **Evaluation:** AUC, F1, precision/recall logged; side-by-side run comparison in Jobs UI  
- **Registry:** top performer registered with metadata (params, metrics, data version)  
- **Handoff:** scoring schema + example requests prepared for integration tests

---

## 3) Clustering — Penguins (K-Means)

This unsupervised workflow segments observations and validates cluster quality before downstream use.  
I combined normalization, k-selection, and post-assignment inspection to ensure stable groupings.

**Key factors**
- **Prep:** Select Columns → Clean Missing → Normalize → Split for holdout checks  
- **Modeling:** K-Means with **silhouette** scoring; elbow method for k pre-selection  
- **Evaluation:** silhouette per k logged; cluster sizes and centroids exported  
- **Usage:** assigned cluster labels persisted for profiling and feature enrichment

---

## 🤖 Automated ML — Baselines & HPO

I ran AutoML for regression/classification to benchmark manual pipelines and explore hyperparameters.  
Results informed model choice and exposed helpful preprocessing defaults.

**Key factors**
- Limits on max trials/runtime; early stopping enabled  
- Metrics (e.g., **AUC_weighted**, **RMSE**) compared to manual runs  
- Best candidate promoted; parameters captured for later SDK replication

---

## 🚀 Deployment & Inference

Selected models were packaged for managed **online endpoints** and validated with sample requests.  
This establishes a thin path from experimentation to consumption by services or dashboards.

**Key factors**
- Reproducible environment (pinned base images/deps)  
- Request/response JSON samples; latency & health checks recorded  
- Roll-forward/rollback ready via model versioning in registry

---

## 📈 Tracking, Versioning, Reproducibility

Every run stores metrics, parameters, and artifacts; failed runs are preserved for auditability.  
Models and datasets are versioned to ensure comparable, explainable outcomes.

**Key factors**
- Run history with comments/tags; **Compare** view for quick A/B checks  
- Dataset URIs + model versions embedded in outputs for lineage  
- Cleanup scripts to stop/scale down compute after experiments

---

## 🔗 Orchestration Blueprint (Data Factory → Azure ML)

For production, I drafted a simple ADF pipeline to schedule data ingestion and execute Azure ML training.  
On success, the job registers a new model and—optionally after approval—updates the deployment.

**Key factors**
- Scheduled trigger → data validation → **Execute Azure ML job**  
- Post-train: register model → gate → deploy/update endpoint  
- Monitoring hook for drift/health; retrain on threshold breach

---


