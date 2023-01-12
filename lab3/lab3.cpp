#include "files.h"
using namespace std;

int main() {
	srand(time(0));
	Index_files a;

	ofstream index_out("index.txt");
	ofstream data_out("data.txt");

	int key, data;
	a.index = new int* [a.proc * a.amount];
	for (int i = 0; i < a.proc * a.amount; i++) {
		a.index[i] = new int[2];
	}

	for (int i = 0; i < a.proc * a.amount; i++) {
		a.index[i][0] = INT_MAX;
		a.index[i][1] = INT_MAX;
	}

	a.filled = new int[a.amount];
	for (int i = 0; i < a.amount; i++) {
		a.filled[i] = 0;
	}

	for (int i = 0; i <= 1000; i++) {
		int in_key = i;
		int in_data = i + 1;
		int s = a.search(in_key);
		if (s == -1) a.insert(in_key, in_data);
	}

	for (int i = 0; i < a.proc * a.amount; i++) {
		index_out << a.index[i][0] << " " << a.index[i][1] << endl;
	}

	for (int i = 0; i < a.size; i++) {
		data_out << a.main_data[i][0] << " " << a.main_data[i][1] << endl;
	}

	int menu;
	while (true) {
		cout << "Choose:\n1 to insert, 2 to search by index, 3 to search by data, 4 to remove, 5 to change, 6 to update, 0 to exit" << endl;
		cin >> menu;

		if (menu == 1) {
			int in_key, in_data;
			cin >> in_key >> in_data;
			if (cin.fail()) {
				cout << "Incorrect entry. Try again:" << endl;
				cin.clear();
				cin.ignore();
				continue;
			}
			int s = a.search(in_key);
			if (s == -1) a.insert(in_key, in_data);
		}
		else if (menu == 2) {
			int s_key, s;
			cin >> s_key;
			if (cin.fail()) {
				cout << "Incorrect entry. Try again:" << endl;
				cin.clear();
				cin.ignore();
				continue;
			}
			s = a.search(s_key);
			if (s != -1) cout << a.main_data[a.index[s][1]][1] << endl;
			else cout << -1 << endl;
		}
		else if (menu == 3) {
			int s_value, s;
			cin >> s_value;
			if (cin.fail()) {
				cout << "Incorrect entry. Try again:" << endl;
				cin.clear();
				cin.ignore();
				continue;
			}
			a.search_data(s_value);
		}
		else if (menu == 4) {
			int r_key;
			cin >> r_key;
			if (cin.fail()) {
				cout << "Incorrect entry. Try again:" << endl;
				cin.clear();
				cin.ignore();
				continue;
			}
			a.delete_key(r_key);
		}
		else if (menu == 5) {
			int in_key, in_data;
			cin >> in_key >> in_data;
			if (cin.fail()) {
				cout << "Incorrect entry. Try again:" << endl;
				cin.clear();
				cin.ignore();
				continue;
			}
			a.change(in_key, in_data);
		}
		else if (menu == 6) {
			index_out.seekp(index_out.beg);
			for (int i = 0; i < a.proc * a.amount; i++) {
				index_out << a.index[i][0] << " " << a.index[i][1] << endl;
			}
			data_out.seekp(data_out.beg);
			for (int i = 0; i < a.size; i++) {
				data_out << a.main_data[i][0] << " " << a.main_data[i][1] << endl;
			}
		}
		else if (menu == 0) break;
	}
	return 0;
}