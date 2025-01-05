SELECT  round(sum(DAILY_FEE)/count(*),0) as 'AVERAGE_FEE' from CAR_RENTAL_COMPANY_CAR where CAR_TYPE='SUV'


-- car type : 세단', 'SUV', '승합차', '트럭', '리무진' 
-- options : ['주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트'  로 구성]
