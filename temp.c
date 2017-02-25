servopd.p = (uint8)(0.004 * (error.present * error.present) + 10);
单排 两边两个横的  中间两个八字的
if(var[0]>var[1])
    {
      number = var[0]-var[1];
      number = (int)(number/adcdanwei);
      if(number>adcm)
      {
        number=adcm;
        servopd.p=11;
        speed_duty1=250;
        speed_duty2=200;
        
      }
      else if(number>10)
      {
        servopd.p=13;
        speed_duty1=250;
        speed_duty2=180;
      }
      else if(number>speednumber)
      {
        servopd.p=9;
        speed_duty1=250;
        speed_duty2=180;
      }
      else
      {
        servopd.p=5;
        speed_duty1=230;
        speed_duty2=230;
      }
      pidduo = adcm+number;
    }
    else
    {
      number = var[1]-var[0];
      number = (int)(number/adcdanwei);
      if(number>adcm)
      {
        number=adcm;
        servopd.p=12;
        speed_duty1=200;
        speed_duty2=250;
        
      }
      else if(number>10)
      {
        servopd.p=13;
        speed_duty1=180;
        speed_duty2=250;
      }
      else if(number>speednumber)
      {
        servopd.p=11;
        speed_duty1=180;
        speed_duty2=250;
      }
      else
      {
        servopd.p=5;
        speed_duty1=230;
        speed_duty2=230;
      }
      pidduo=adcm-number;
