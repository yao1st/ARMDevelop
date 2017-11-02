#include "sys.h"
#include "delay.h"
#include "timer.h"
#include "led.h"
#include "dirc.h"
#include "usart.h"


u16 TIM2CC1 = 500;
u16 TIM2CC2 = 250;
u16 step_a =0;
u16 step_d = 10000;

u8 mystrcmp(u8 *str1, u8 *str2, u8 len)
{
	u8 i = 0;
	for(i = 0; i<len; i++)
	{
		if (str1[i] != str2[i])
			return 1;
	}
	return 0;
}

int main(void)
{
	u8 i = 0;
	u8 dirport[MOTORNUM] = {1, 2};
	u8 dir[MOTORNUM] = {0, 1};
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	
	delay_init();
	LED_Init();
	uart_init(115200);
	for (i=0;i<30; i++)
	{
		LED1 = !LED1;
		delay_ms(100);
	}
	
	printf(" Motor Config...\r\n");
	
	DIR_GPIO_Configuration();
	Set_ALL_Dir_GPIO(dirport, dir);
	
	TIM_GPIO_Config_Init();
	TIM_NVIC_Configuration();
	TIM_Congfig_Init(71);
	
	printf(" Please send command\r\n");
	while(1)
	{
		if(USART_RX_STA & 0x8000)
		{
			u8 len = USART_RX_STA & 0x3f;
			u8 command[] = "ok";
			if (mystrcmp(USART_RX_BUF, command, len) == 0)
			{
				break;
			}
		}
		delay_ms(100);
		LED0 = !LED0;
	}
	printf(" Motor Startup\r\n");
	TIM_Startup();
	while(1)
	{
		LED0 = !LED0;
		delay_ms(1000);
	}
}


