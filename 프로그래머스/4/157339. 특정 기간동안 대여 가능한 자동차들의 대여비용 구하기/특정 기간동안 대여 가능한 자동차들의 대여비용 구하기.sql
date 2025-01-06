-- CAR_TYPE: '세단', 'SUV', '승합차', '트럭', '리무진'
-- OPTIONS: '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 
-- DURATION_TYPE: 7, 30, 90

select car_id, car_type, fee from 
(
    select  car.car_id, car.car_type,duration_type,daily_fee,discount_rate,
            round(daily_fee*(1-discount_rate/100)*30,0) as fee
    from CAR_RENTAL_COMPANY_CAR car
    inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
    on car.car_type = plan.car_type
    where car.car_type in ('세단','SUV')
    and plan.duration_type = '30일 이상'
    and car.car_id not in 
                    (select car_id 
                        from CAR_RENTAL_COMPANY_RENTAL_HISTORY history
                        where history.start_date <= '2022-11-30' 
                            and  history.end_date >= '2022-11-01'
                    )
) result
where fee >= 500000 and fee < 2000000
order by fee desc, car_type asc, car_id desc