function calculateDaysBetweenDates(begin, end) {
  const millisecondsPerDay = 86400000;
  const beginDate = new Date(begin);
  const endDate = new Date(end);
  const difference = endDate - beginDate;
  return Math.floor(difference / millisecondsPerDay);
}
