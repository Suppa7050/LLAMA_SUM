import React from 'react';

const Summary = ({text, flag}) => {
  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Summary</h1>
      {flag?(
        <div>
          <p style={styles.text}>{text}</p>
          <div className="loading-container">
            <div className="spinner-border" role="status"></div>
            <div className='loading_title'>Loading...</div>
          </div>
        </div>
      ):(
        <p style={styles.text}>{text}</p>
      )}
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    padding: '20px',
    backgroundColor: '#f0f0f0',
    // borderRadius: '0px 20px',
    height: '100%',
    // boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
  },
  heading: {
    fontSize: '2em',
    color: '#333',
    borderBottom: '2px solid #333',
    paddingBottom: '10px',
    marginBottom: '20px',
  },
  text: {
    whiteSpace: 'pre-line',
    fontSize: '1.2em',
    color: '#555',
    lineHeight: '1.5',
  },
};

export default Summary;
