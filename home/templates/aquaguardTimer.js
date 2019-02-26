 //put the id of 

                    var timerId="time";


                    var min=0,sec=0,hr=0;
                    var timerinterval;
                    var autosaveCounter=0;
                    function startTimer()
                    {
                        autosaveCounter=0;
                        if(localStorage['startTime']==undefined)
                            loadStartTime();
                        elapsedTime=JSON.parse(localStorage['elapsedTime']);
                        sec=elapsedTime['sec'];
                        min=elapsedTime['min'];
                        hr=elapsedTime['hour'];
                        console.log(localStorage);
                        timerinterval=setInterval(function(){
                            //executing work background time related work to be executed every second
                            sec+=1;
                           
                            if(sec>60)
                            {min+=1;sec=0;autosaveCounter+=1;}
                            if(min>60)
                            {hr+=1;min=0;}
                            document.getElementById("time").innerText=hr+":"+min+":"+sec;
                            
                            if(autosaveCounter>2)
                            {
                                autosaveTimer();
                                autosaveCounter=0;
                                console.log("auto saved");
                                console.log(localStorage);
                            }

                        },1000);
                        
                    }
                    function stopTimer()
                    {
                    localStorage.removeItem("elapsedTime");
                    localStorage.removeItem("startTime");
                    localStorage.removeItem("pausedTime");
                    }
        
                    
        
        
                    //loading the time for first time during login
                    function loadStartTime()
                    {
                        today=new Date();
                        data={}
                        data['hour']=today.getHours();
                        data['min']=today.getMinutes();
                        data['sec']=today.getSeconds();
                        localStorage['startTime']=JSON.stringify(data);
                        localStorage['pausedTime']="[]";
                        data['hour']=0;
                        data['min']=0;
                        data['sec']=0;
                        localStorage['elapsedTime']=JSON.stringify(data);
                        console.log(localStorage);
                    }
        
                    function pauseTimer()
                    {
                        clearInterval(timerinterval);
                        timeEvents=JSON.parse(localStorage['pausedTime']);
                        today=new Date();
                        //save current time
                        data={}
                        data['hour']=today.getHours();
                        data['min']=today.getMinutes();
                        data['sec']=today.getSeconds();
                        console.log("time events");
                        console.log(timeEvents);
                        timeEvents.push(data);
                        console.log(timeEvents);
                        localStorage['pausedTime']=JSON.stringify(timeEvents);
        
                        //save total elapsed time
                        data={};
                        data['hour']=hr;
                        data['min']=min;
                        data['sec']=sec;
                        console.log(data);
                        localStorage['elapsedTime']=JSON.stringify(data);
                        console.log(localStorage);
                        
                    }

                function autosaveTimer()
                {
                    data={};
                        data['hour']=hr;
                        data['min']=min;
                        data['sec']=sec;
                        console.log(data);
                        localStorage['elapsedTime']=JSON.stringify(data);
                }