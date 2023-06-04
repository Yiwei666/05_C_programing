const readline = require('readline');
const moment = require('moment');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('请输入未来时间点（格式：日子-小时-分钟，例如：05-17-30）：', (input_str) => {
  const [day, hour, minute] = input_str.split('-');

  const future_date = moment().set({
    'date': parseInt(day),
    'hour': parseInt(hour),
    'minute': parseInt(minute),
    'second': 0,
    'millisecond': 0
  });

  setInterval(() => {
    const current_date = moment();
    const time_left = moment.duration(future_date.diff(current_date));

    const hours = time_left.hours().toString().padStart(2, '0');
    const minutes = time_left.minutes().toString().padStart(2, '0');
    const seconds = time_left.seconds().toString().padStart(2, '0');

    console.log(`距离未来时间点还有：${hours}:${minutes}:${seconds}`);
  }, 5000);
});