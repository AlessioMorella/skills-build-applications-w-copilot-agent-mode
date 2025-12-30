
const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard API endpoint:', endpoint);
        console.log('Fetched leaderboard data:', data);
        setLeaderboard(data.results ? data.results : data);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  const allKeys = Array.from(
    leaderboard.reduce((keys, item) => {
      Object.keys(item).forEach(k => keys.add(k));
      return keys;
    }, new Set())
  );

  return (
    <div className="container mt-4">
      <h1 className="mb-4 display-5">Leaderboard</h1>
      <div className="card shadow">
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-hover align-middle">
              <thead className="table-dark">
                <tr>
                  {allKeys.length === 0 ? <th>No Data</th> : allKeys.map(key => <th key={key}>{key}</th>)}
                </tr>
              </thead>
              <tbody>
                {leaderboard.length === 0 ? (
                  <tr><td colSpan={allKeys.length}>No leaderboard data found.</td></tr>
                ) : (
                  leaderboard.map((entry, idx) => (
                    <tr key={entry.id || idx}>
                      {allKeys.map(key => <td key={key}>{String(entry[key])}</td>)}
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
