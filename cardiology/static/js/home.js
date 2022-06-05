@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;1,300;1,400;1,500&display=swap');

:root{
  --darkred:#852126;
  --red:#df0e18;
}

*{
  font-family: 'Roboto', sans-serif;
  text-transform: capitalize;
  text-decoration: none;
  outline: none;
  margin: 0; padding: 0;
  box-sizing: border-box;
}

*::selection{
  background:var(--darkred);
  color:#fff;
}

html{
  font-size: 62.5%;
  overflow-x: hidden;
}

.heading{
  font-size: 5rem;
  color:var(--darkred);
  text-align: center;
  padding:0 1rem;
  padding-top: 6rem;
  letter-spacing: .2rem;
  font-weight: 500;
}
.heading span{
    font-size: 5rem;
    color:var(--red);
    text-align: center;
    padding:0 1rem;
    padding-top: 6rem;
    letter-spacing: .2rem;
    font-weight: 500;
  }

.title{
  padding:0 1rem;
  font-size: 2rem;
  text-align: center;
  font-weight: 400;
  color:#aaa;
}

header{
  width:96%;
  background:#fff;
  position: fixed;
  top:2rem; left:50%;
  transform: translateX(-50%);
  border-radius: 5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding:1rem 2rem;
  z-index: 1000;
  transition: .2s;
}

.header-active{
  top:0;
  width: 100%;
  border-radius: 0;
  box-shadow: 0 .1rem .3rem rgba(0,0,0,.3);
}

header .navbar ul{
  display: flex;
  align-items: center;
  justify-content: space-between;
  list-style: none;
}

header .navbar ul li{
  margin:0 1rem;
}

header .navbar ul li a{
  font-size: 2rem;
  color:var(--darkred);
  transition: .2s;
}

header .navbar ul li .active,
header .navbar ul li a:hover{
  color:var(--red);
}

header .logo{
  font-size: 2.5rem;
  color: var(--red);
  text-transform: uppercase;
}

header .logo i{
  color:var(--darkred);
  padding:0 .2rem;
}

header .fa-bars{
  font-size: 3rem;
  color:var(--darkred);
  cursor: pointer;
  display: none;
  transition: .2s;
}

.home{
  min-height: 100vh;
  background:linear-gradient(rgba(126, 71, 71, 0.8),rgba(246, 164, 164, 0.8)), url(../images/image2.jpg) no-repeat;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  z-index: 0;
  overflow:hidden;
  position: relative;
}

.home .content{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-flow: column;
  padding-top: 14rem;
  padding-bottom: 8rem;
  text-align: center;
}

.home .content h1{
  font-size: 5rem;
  color: #fff;
  padding:0 1rem;
  text-shadow: 0 .3rem .5rem rgba(0,0,0,.3);
  text-transform: uppercase;
}

.home .content p{
  font-size: 2rem;
  color:#eee;
  padding:1rem 25rem;
}

.home .content button{
  height:4rem;
  width:20rem;
  border-radius: 5rem;
  background:var(--darkred);
  color:#fff;
  font-size: 2rem;
  cursor: pointer;
  transition: .2s;
  border:none;
  box-shadow: 0 .3rem 1rem rgba(0,0,0,.3);
}

.home .content button:hover{
  letter-spacing: .2rem;
  background:var(--red);
}

.home .box-container{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.home .box-container .box{
  height:20rem;
  width:25rem;
  background:#fff;
  text-align: center;
  border-radius: 1rem;
  box-shadow: 0 .3rem .5rem rgba(0,0,0,.5);
  margin: 2rem;
  cursor: pointer;
}

.home .box-container .box i{
  height:6rem;
  width:6rem;
  line-height: 6rem;
  text-align: center;
  border-radius: 50%;
  color:#fff;
  background:var(--red);
  font-size: 3rem;
  margin:2rem 0;
  transition: .2s;
}

.home .box-container .box h3{
  font-size: 2rem;
  color:var(--darkred);
  transition: .2s;
}

.home .box-container .box p{
  font-size: 1.3rem;
  padding:.7rem 2rem;
  color:#666;
}

.home .box-container .box:hover i{
  background:var(--darkred);
}

.home .box-container .box:hover h3{
  color:var(--red);
}

.home::before{
  content: '';
  position: absolute;
  bottom:-25rem; left:50%;
  transform: translateX(-50%);
  border-top: 70vh solid #fff;
  width:120%;
  border-radius: 50%;
  z-index: -1;
}

.about{
    background:#f9f9f9;
}
.about .row{
  display: flex;
  justify-content: center;
  align-items: center;
}

.about .row .image img{
  height:70vh;
  width:50vw;
  padding-right: 2rem;
  padding-top: 3rem;
  padding-bottom: 3rem;
}

.about .row .content{
  padding-left: 5rem;

}

.about .row .content h3{
  font-size: 3.5rem;
  color:var(--darkred);
}

.about .row .content p{
  font-size: 2rem;
  color:#999;
  padding:2rem 2rem;
}

.about .row .content button{
  height:4rem;
  width:20rem;
  background:var(--red);
  color:#fff;
  border:none;
  border-radius: 5rem;
  box-shadow: 0 .3rem 1rem rgba(0,0,0,.3);
  cursor: pointer;
  font-size: 2rem;
  transition: .2s;
}

.about .row .content button:hover{
  letter-spacing: .2rem;
  opacity: .8;
  background:var(--darkred);
}

.doctor {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
    -webkit-box-pack: center;
        -ms-flex-pack: center;
            justify-content: center;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-flow: column;
            flex-flow: column;
    width: 100vw;
}

.doctor .doctor-container {
    width: 90%;
}

.doctor .doctor-container .owl-nav .owl-next, .doctor .doctor-container .owl-nav .owl-prev {
    position: absolute;
    top: 50%;
    -webkit-transform: translateY(-50%);
            transform: translateY(-50%);
    color: #EB4D4B;
    font-size: 6rem;
    background: none;
    border: none;
    outline: none;
}

.doctor .doctor-container .owl-nav .owl-next {
    right: 1rem;
}

.doctor .doctor-container .owl-nav .owl-prev {
    left: 1rem;
}
  .doctor .doctor-container .doctor-slider .doctor-card {
    height: 40rem;
    width: 30rem;
    margin: 2rem auto;
    -webkit-box-shadow: 0 0 0.3rem rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 0.3rem rgba(0, 0, 0, 0.5);
    border-radius: .5rem;
    position: relative;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .image {
    height: 75%;
    width: 100%;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .image img {
    height: 100%;
    width: 100%;
    -o-object-fit: cover;
       object-fit: cover;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .content {
    height: 25%;
    width: 100%;
    text-align: center;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .content h3 {
    font-size: 3rem;
    color: var(--darkred);
    padding-top: 3rem;
  }


  .doctor .doctor-container .doctor-slider .doctor-card .info {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background: rgb(117, 115, 115);
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
    -webkit-box-pack: center;
        -ms-flex-pack: center;
            justify-content: center;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
        -ms-flex-flow: column;
            flex-flow: column;
    -webkit-transition-delay: .2s;
            transition-delay: .2s;
    -webkit-transform: scale(0);
            transform: scale(0);
  }

  .doctor .doctor-container .doctor-slider .doctor-card .info h4 {
    font-size: 4rem;
    color: #fff;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .info p {
    font-size: 1.2rem;
    padding: 1rem 2rem;
    color: #ccc;
    text-align: center;
  }



  .doctor .doctor-container .doctor-slider .doctor-card .info .share {
    margin-top: 4rem;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .info .share a {
    font-size: 2rem;
    height: 4rem;
    width: 4rem;
    line-height: 4rem;
    text-align: center;
    background: #fff;
    color: #EB4D4B;
    margin: 0 .5rem;
    border-radius: 5rem;
  }

  .doctor .doctor-container .doctor-slider .doctor-card .info .share a:hover {
    text-decoration: none;
    background: #EB4D4B;
    color: #fff;
  }

.doctor .doctor-container .doctor-slider .doctor-card:hover .info {
    -webkit-transform: scale(1);
            transform: scale(1);
  }

.owl-theme .owl-nav [class*=owl-]:hover {
    background: #fff!important;
    color: var(--red)!important;
    text-decoration: none;
}


.services{
    background:#f9f9f9;
}

.services .box-container{
  width:85%;
  display: flex;
  justify-content: center;
  margin:0 auto;
  padding-top: 4rem;
  flex-wrap: wrap;
}

.services .box-container .box{
  height:18rem;
  width:25rem;
  margin:3.5rem 2rem;
  text-align: center;
  border-radius: 1rem;
  box-shadow: .3rem .3rem 0 .1rem var(--red),
              .5rem .5rem .5rem rgba(0,0,0,.3);
}

.services .box-container .box i{
  height:10rem;
  width:10rem;
  line-height: 8rem;
  text-align: center;
  color:#fff;
  border-radius: 50%;
  background:var(--darkred);
  margin-top: -4rem;
  border:1rem solid #fff;
  border-left:1rem solid var(--darkred);
  border-right:1rem solid var(--darkred);
  box-shadow: 0 0 0 1rem #fff inset;
  font-size: 3.5rem;
}

.services .box-container .box h3{
  font-size: 2rem;
  color:var(--red);
}

.services .box-container .box p{
  font-size: 1.5rem;
  color:#999;
  padding:1rem 0;
}

.book .row{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap:2rem;
}

.book .row .image{
    flex:1 1 45rem;
}

.book .row .image img{
    width: 95%;
    padding-top: 4rem;
    padding-bottom: 4rem;
    padding-left: 9rem;
}

.book .row .content{
    flex:1 1 45rem;
    padding-left: 5rem;
    padding-bottom: 5rem;
}

.book .row .content h3{
    font-size: 3rem;
    line-height: 1.8;
    color:var(--darkred);
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.book .row .content button{
    height:4rem;
    width:20rem;
    background:var(--red);
    color:#fff;
    border:none;
    border-radius: 5rem;
    box-shadow: 0 .3rem 1rem rgba(0,0,0,.3);
    cursor: pointer;
    font-size: 2rem;
    transition: .2s;
  }

  .book .row .content button:hover{
    letter-spacing: .2rem;
    opacity: .8;
    background:var(--darkred);
  }



  .contact .row{
    display: flex;
    align-items: center;
    justify-content: space-around;
  }

  .contact .row .contact-info .box{
    margin:4rem 2rem;
  }

  .contact .row .contact-info .box h3{
    font-size: 2rem;
    color:#333;
  }

  .contact .row .contact-info .box h3 i{
    color:var(--red);
  }

  .contact .row .contact-info .box p{
    padding-left: 3rem;
    font-size: 1.7rem;
    color:#aaa;
  }

  .contact .row .contact-form-container{
    width:50%;
  }

  .contact .row .contact-form-container h3{
    font-size: 4rem;
    padding-top: 4rem;
    color:var(--darkred);
  }

  .contact .row .contact-form-container .inputBox{
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }

  .contact .row .contact-form-container .inputBox input{
    width: 49%;
  }

  .contact .row .contact-form-container form input, textarea{
    outline: none;
    border:.2rem solid var(--red);
    height:4rem;
    background:#fff;
    padding:0 1rem;
    margin:1rem 0;
    font-size: 1.8rem;
  }

  .contact .row .contact-form-container form textarea{
    width:100%;
    padding:1rem;
    resize: none;
    height:20%;
  }

  .contact .row .contact-form-container form input[type="submit"]{
    color:var(--red);
    border:.2rem solid var(--red);
    cursor: pointer;
    transition: .2s;
    width:20rem;
  }

  .contact .row .contact-form-container form input[type="submit"]:hover{
    color:#fff;
    background:var(--red);
  }
.footer{
  text-align: center;
}

.footer .icons{
  padding:3rem 0;
}

.footer .icons a{
  height:4.5rem;
  width: 4.5rem;
  line-height: 4.2rem;
  text-align: center;
  border-radius: 50%;
  color:var(--red);
  border:.2rem solid var(--red);
  font-size: 2rem;
  margin:0 .1rem;
  transition: .2s linear;
}

.footer .icons a:hover{
  color:#fff;
  background:var(--darkred);
  border-color: var(--darkred);
}


.footer .credit{
  font-size: 2rem;
  border-top: .1rem solid #999;
  margin:0 auto;
  margin-bottom: 2rem;
  color:#666;
  width:90%;
  padding:1rem 0;
}

.footer .credit span{
  color:var(--red);
}

header .fa-times{
  transform: rotate(180deg);
  color:var(--red);
}

/* media queries  */

@media (max-width:768px){

  html{
    font-size: 55%;
  }

  header .fa-bars{
    display: block;
  }

  header .navbar{
    position: fixed;
    top:-100rem; left:0;
    width:100%;
    background:#fff;
    border-radius: 1rem;
    opacity: 0;
    transition: .2s linear;
  }

  header .navbar ul{
    flex-flow: column;
    padding:2rem 0;
  }

  header .navbar ul li{
    margin:1rem 0;
    width:100%;
    text-align: center;
  }

  header .navbar ul li a{
    font-size: 3rem;
    display: block;
  }

  header .nav-toggle{
    top:5.5rem;
    opacity: 1;
  }

  .home .content p{
    padding:1.5rem 2rem;
  }

  .home::before{
    display: none;
  }

  .about .row{
    flex-flow: column-reverse;
  }

  .about .row .image img{
    height:60vh;
    width:90vw;
  }

  .about .row .content{
    padding:0 2.5rem;
  }

  .services .box-container{
    width:100%;
  }

  .contact .row{
    flex-flow: column;
  }

  .contact .row .image img{
    height:50vh;
    width:90vw;
  }

  .contact .row .form-container{
    width:90%;
    padding:0;
  }
}