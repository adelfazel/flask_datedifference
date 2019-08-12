function correctDateString(dateString) {
  const splited = dateString.split("-");
  const year = splited[0]
  const month = splited[1]
  const day = splited[2]
  return `${day}/${month}/${year}`
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#form').onsubmit = () => {
    const request = new XMLHttpRequest();
    const firstDate = document.querySelector('input[name="firstDate"]').value;
    const secondDate = document.querySelector('input[name="secondDate"]').value;
    var data = new FormData();

    data.append('FD', correctDateString(firstDate));
    data.append('SD', correctDateString(secondDate));

    request.open('POST', '/getdiff');
    request.onload = () => {
      const response = JSON.parse(request.responseText);
      if (response.success) {
        document.querySelector('#result').innerHTML = `There are ${response.Diff} days between ${firstDate} and ${secondDate}`;
      } else {
        document.querySelector('#result').innerHTML = `Unable to handle input`;
      }
    }
    request.send(data);
    return false;
  }
});
