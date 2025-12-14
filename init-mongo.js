db = db.getSiblingDB("pricing_logs");

db.createCollection("simulation_logs");
db.simulation_logs.createIndex({ product_code: 1, created_at: -1 });
db.simulation_logs.createIndex({ session_id: 1 });
db.simulation_logs.createIndex(
  { created_at: 1 },
  { expireAfterSeconds: 7776000 },
);

db.createCollection("access_logs");
db.access_logs.createIndex({ endpoint: 1, created_at: -1 });
db.access_logs.createIndex({ created_at: 1 }, { expireAfterSeconds: 2592000 });
