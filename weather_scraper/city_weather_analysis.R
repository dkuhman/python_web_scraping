#Creator: Daniel Kuhman
#Date Created: 2020-05-10
#Github: https://github.com/dkuhman

#install.packages('ggjoy')
library('tidyverse')
library("ggplot2")
library('ggjoy')

rm(list = ls())

#Load data - point to cit_weather_2019.csv
mydata_path <- file.choose(new = FALSE)
mydata <- read.csv(mydata_path)
rm(mydata_path)

#Prep Data
mydata<-mydata %>% 
  select(city,week_day,date,time1,temp_low1,temp_high1,
        time2,temp_low2,temp_high2,
        time3,temp_low3,temp_high3,
        time4,temp_low4,temp_high4)

mydata<-mydata[complete.cases(mydata),]

mydata$date<-as.character(mydata$date)
mydata$Month<-substr(mydata$date,2,4)
mydata$Month<-as.factor(mydata$Month)

levels(mydata$city)[levels(mydata$city)=="birmingham"] <- "Birmingham"
levels(mydata$city)[levels(mydata$city)=='cleveland']<-'Cleveland'

mydata$city<-as.factor(mydata$city)
mydata$temp_low1<-as.numeric(as.character(mydata$temp_low1))
mydata$temp_low2<-as.numeric(as.character(mydata$temp_low2))
mydata$temp_low3<-as.numeric(as.character(mydata$temp_low3))
mydata$temp_low4<-as.numeric(as.character(mydata$temp_low4))


#Re-order factor levels
mydata$Month<-factor(mydata$Month,
                           levels = c("Jan", "Feb", "Mar",
                                      "Apr", "May", "Jun",
                                      "Jul", "Aug", "Sep",
                                      "Oct", "Nov", "Dec"))

#Plot
ggplot(mydata, aes(y=Month, x=temp_high3))+
  geom_joy(scale=1.5, aes(fill=city), alpha=0.4, lwd=0.5)+
  theme_classic()+
  scale_fill_manual(values=c('#CC0000','#003399'))+
  labs(y="Month",
       x="Temperature (deg. F)")+
  guides(fill=guide_legend(title="City"))+
  theme(
    axis.title.x = element_text(size=25, color='black', face='bold',
                              margin = margin(t=30,r=0,b=0,l=0)),
    axis.title.y = element_text(size=25, color='black', face='bold',
                                margin = margin(t=0,r=30,b=0,l=0)),
    axis.text = element_text(size=18, color='black'),
    legend.title = element_text(size = 18, color = 'black', face = 'bold'),
    legend.text = element_text(size = 18, color = 'black')
  )
