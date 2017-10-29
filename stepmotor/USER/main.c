#include "sys.h"
#include "delay.h"
#include "timer.h"
#include "led.h"
#include "usart.h"

int main(void)
{
	u16 arr = 4;
	u16 psc = 7199;
	
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	delay_init();
	LED_Init();
	uart_init(115200);
	delay_ms(3000);
	TIM2_Int_Init(arr, psc);
	while(1)
	{
		LED0 = !LED0;
		delay_ms(1000);
	}
}

