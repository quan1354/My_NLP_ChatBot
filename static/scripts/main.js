function textme(){
    let screen2 = document.getElementById("chatbot")
    screen2.classList.remove("chatbot")
    screen2.setAttribute("class","container")
    screen2.setAttribute("id","dom")
    screen2.innerHTML=`
                <div class="head">
                    <h4 class="title">Chatbot</h4>
                    <button class="icon" id="reduire" onclick="icon()">-</button>
                </div>
                <!--start body : conversation -->
                <div class="body">
                    <div class="common ">
                            <p  class="robottalk">
                                    Hello, How can I help ?
                            </p>                
                    </div>
                <!--   <div class="usermsg">Je veux qlq chose </div> -->

                </div>
                <!--end body : conversation -->
                <div class="foot">
                    <input type="text"   id="msg">
                    <img   id="send"  />
                </div>
           

    `
    



     /* for input */
     let send = document.getElementById("send")
     let sms = document.getElementById("msg")
     /* for output*/
     let body = document.querySelector(".body")
     /* ajax  */
     let reponse = "hi"
     /* end ajax */
    /* click enter */
    sms.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            let usersms = document.createElement("div")
            usersms.setAttribute("class","common")
            //
// python function 
            $.ajax({
                url:`/response?langage=${sms.value}`,
                type:"POST",
            //   data:$('random_decimal1').serialize(),
                dataType : "json" , 
                success: function(data){
                    reponse = data
                    msg.value=""
                }
            })
            //
            usersms.innerHTML=`<p class="usermsg "> ${sms.value}</p>`
            body.appendChild(usersms)
           sms.value=""
            /* answer */
            let robotanswer = document.createElement("div")
            robotanswer.setAttribute("class","common")
            setTimeout(function(){
                robotanswer.innerHTML=`<p class="robottalk ">${reponse}</p>`
             },1000)
            body.appendChild(robotanswer)
            body.scrollTop=body.scrollHeight - (body.clientHeight )
           // setTimeout(() => , 2000);        }
    
    }    })
    /* end */


// click
     send.addEventListener("click",function(){
         let usersms = document.createElement("div")
         usersms.setAttribute("class","common")
        
          //
            // python function 
            $.ajax({
                url:`/response?langage=${sms.value}`,
                type:"POST",
            //   data:$('random_decimal1').serialize(),
                dataType : "json" , 
                success: function(data){
                    reponse = data
                    msg.value=""
                }
            })
            //
         usersms.innerHTML=`<p class="usermsg "> ${sms.value}</p>`
         body.appendChild(usersms)
        sms.value=""
         /* answer */
         let robotanswer = document.createElement("div")
         robotanswer.setAttribute("class","common")
         setTimeout(function(){
            robotanswer.innerHTML=`<p class="robottalk ">${reponse}</p>`
         },1000)
         body.appendChild(robotanswer)
         body.scrollTop=body.scrollHeight - (body.clientHeight )
        // setTimeout(() => , 2000);

 
 
     })


     /* scroll Y */
    

    /* end scroll */
 
}







function icon(){ 
    let screen1 = document.getElementById("dom")

    screen1.classList.remove("container")
    screen1.setAttribute("class","chatbot")
    screen1.setAttribute("id","chatbot")
    screen1.innerHTML=`
    <div class="profil">
                <img  class="img-bot"  id="imgbot" onclick="textme()">
            </div>
    `

}

