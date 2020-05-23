#include <stdio.h>
#include <pthread.h>
#include <time.h>
#include <unistd.h>

int secs, mins, hrs;

void *seconds() {
	while(1) {
		sleep(1);
		secs++;
	}
}


void *minutes() {
	while(1) {
		if(secs == 60) {
			secs = 0;
			mins++;
		}
	}
}

void *hour() {
	while(1) {
		if(mins == 60){
			mins = 0;
			hrs++;
		}
	}
}

void *print() {
	while(1) {
		printf("\r%02d : %02d : %02d", hrs, mins, secs);
	}
}

int main() {
	pthread_t t1,t2,t3,t4;

	time_t cur_time;
	time(&cur_time);
	struct tm *local = localtime(&cur_time);

	hrs = local->tm_hour;
	mins = local->tm_min;
	secs = local->tm_sec;

	printf("\nCurrent Time\n");

	pthread_create(&t1, NULL, seconds, NULL);
	pthread_create(&t2, NULL, minutes, NULL);
	pthread_create(&t3, NULL, hour, NULL);
	pthread_create(&t4, NULL, print, NULL);

	pthread_join(t1, NULL);
	pthread_join(t2, NULL);
	pthread_join(t3, NULL);
	pthread_join(t4, NULL);

	return 0;
}
