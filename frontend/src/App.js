import React, { useState } from "react";

function App() {
  const [formData, setFormData] = useState({
    industry: "",
    company_size: "",
    region: "",
    num_contacts: "",
    engagement_score: "",
    source: "",
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);

    try {
      const response = await fetch("https://lead-scoring-system.onrender.com/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ...formData,
          company_size: parseInt(formData.company_size),
          num_contacts: parseInt(formData.num_contacts),
          engagement_score: parseInt(formData.engagement_score),
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to get prediction from server.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Please try again.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-center mb-4">🔍 Smart Lead Scoring</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input className="form-control" name="industry" placeholder="Industry" onChange={handleChange} required />
          </div>
          <div className="mb-3">
            <input className="form-control" type="number" name="company_size" placeholder="Company Size" onChange={handleChange} required />
          </div>
          <div className="mb-3">
            <input className="form-control" name="region" placeholder="Region" onChange={handleChange} required />
          </div>
          <div className="mb-3">
            <input className="form-control" type="number" name="num_contacts" placeholder="Number of Contacts" onChange={handleChange} required />
          </div>
          <div className="mb-3">
            <input className="form-control" type="number" name="engagement_score" placeholder="Engagement Score" onChange={handleChange} required />
          </div>
          <div className="mb-3">
            <input className="form-control" name="source" placeholder="Lead Source" onChange={handleChange} required />
          </div>
          <button type="submit" className="btn btn-primary w-100">Predict</button>
        </form>

        {result && (
          <div className="alert alert-success mt-4">
            <h5>Prediction Result</h5>
            <p><strong>Conversion Probability:</strong> {result.score}</p>
            <p><strong>Label:</strong> <span className="fw-bold text-primary">{result.label}</span></p>
          </div>
        )}

        {error && (
          <div className="alert alert-danger mt-4">
            <p>{error}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
