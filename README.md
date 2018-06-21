# DevMeetup  [![Travis](https://travis-ci.org/dev-meetup/dev-meetup.github.io.svg?branch=master)](https://travis-ci.org/dev-meetup/dev-meetup.github.io)

개발 관련 밋업, 세미나 정보 공유 페이지


## 이벤트 추가하기
- `data/events.json`에 데이터 추가
- `master` branch 대상으로 추가

```json
{
  "events":[
    {
      "id": 1,
      "title": "GDG Korea WebTech meetup",
      "url": "https://gdg-korea-webtech.firebaseapp.com/events/meetup-20170223/",
      "start": "2017-02-23 19:30:00",
      "end": "2017-02-23 22:00:00",
      "address":"서울특별시 강남구 논현1동 15-11 Fast Campus 별관 MH bld. 3rd floor",
      "tags":"google, gdg, gdgkorea", 
      "pay_amount": "1,000 ~ 29,500" 
    },
   ...
]
}
```

- pull request 혹은 commit 후 반영됨.

## TODO 
- [x] mobile support
- [ ] subscribe email 
- [ ] dump google calendar ics
- [ ] search hashtag 

## event source 
- http://onoffmix.com
- https://www.meetup.com
- https://festa.io
- facebook group/timeline
- https://tacademy.sktechx.com


### References :
- [React](https://facebook.github.io/react/)
- [bootstarap](getbootstrap.com)
- [material-kit](https://www.creative-tim.com/)
- [fullcalendar](https://fullcalendar.io)
- [hammer.js](http://hammerjs.github.io/)
