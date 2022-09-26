function ProgressBar(props) {
  return (
    <div className = "progressBarContainer">
      <div id = "progressBarLabel">Progress</div>
      <div id = "progressBarSubdivider">
        <div id = "PB1" className = "progressBarSegment"></div>
        <div id = "PB2" className = "progressBarSegment"></div>
        <div id = "PB3" className = "progressBarSegment"></div>
      </div>
    </div>
  );
}

export default ProgressBar;
