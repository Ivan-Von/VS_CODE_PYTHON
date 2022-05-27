#include <iostream>
#include <queue>
using namespace std;
int r, c;
const int N = 45;
char mp[N][N];
typedef pair<int, int>PII;
#define x first
#define y second
int vis[N][N];
int flag;
int dis[N][N];//距离
int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};

int dbfs() {
	queue<PII>q1, q2;//q1为从前往后搜，q2为从后往前搜
	dis[1][1] = 1;
	dis[r][c] = 1;
	vis[1][1] = 1;//q1标记为1
	vis[r][c] = 2;//q2标记为2
	//如果某状态下，当前节点和准备扩展节点的状态相加为3，
	//说明相遇
	q1.push({1, 1});
	q2.push({r, c});
	PII t;
	while (q1.size() && q2.size()) {
		if (q1.size() < q2.size()) {//每次扩展搜索树小的队列 flag=1表示从前往后搜的队列，flag=0表示从后往前搜的队列
			t = q1.front();
			q1.pop();
			flag = 1;//q1标记为1
		}
        else {
			t = q2.front();
			q2.pop();
			flag = 0;//q2标记为0
		}
		for (int i = 0; i < 4; i++) {
			int xx = t.x + dx[i];
			int yy = t.y + dy[i];
			if (xx >= 1 && xx <= r && yy >= 1 && yy <= c && mp[xx][yy] == '.'){
				if (!dis[xx][yy]){
					if (flag) {
						vis[xx][yy] = 1;
						dis[xx][yy] = dis[t.x][t.y] + 1;
						q1.push({xx, yy});
					} else {
						vis[xx][yy] = 2;
						dis[xx][yy] = dis[t.x][t.y] + 1;
						q2.push({xx, yy});
					} 
                } else {
                    if (vis[xx][yy] + vis[t.x][t.y] == 3){//相遇
                        return dis[xx][yy] + dis[t.x][t.y];
                    }
                }
		    }
        }
    }
    return -1;
}


int main() {
	cin >> r >> c;
	for (int i = 1; i <= r; i++)
		for (int j = 1; j <= c; j++)
			cin >> mp[i][j];

	cout << dbfs() << endl;
	return 0;
}