#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

struct Process {
    string id;
    int burst;
    int arrival;
    int queue;
    int priority;
    int remaining;
    int inputOrder;
};

struct Metrics {
    double turnaroundAvg = 0.0;
    double waitingAvg = 0.0;
};

string trim(const string& value) {
    const string whitespace = " \t\r\n";
    const size_t start = value.find_first_not_of(whitespace);
    if (start == string::npos) {
        return "";
    }
    const size_t end = value.find_last_not_of(whitespace);
    return value.substr(start, end - start + 1);
}

vector<string> splitSemicolonLine(const string& line) {
    vector<string> fields;
    string field;
    stringstream ss(line);
    while (getline(ss, field, ';')) {
        fields.push_back(trim(field));
    }
    return fields;
}

int parseIntField(const string& value, const string& fieldName, const string& filePath, int lineNumber) {
    try {
        size_t pos = 0;
        const int parsed = stoi(value, &pos);
        if (pos != value.size()) {
            throw invalid_argument("extra");
        }
        return parsed;
    } catch (const exception&) {
        throw runtime_error(filePath + ":" + to_string(lineNumber) +
                            " invalid " + fieldName + " value: '" + value + "'");
    }
}

vector<Process> loadProcessesFromFile(const string& filePath) {
    ifstream input(filePath);
    if (!input.is_open()) {
        throw runtime_error("Could not open input file: " + filePath);
    }

    vector<Process> processes;
    string rawLine;
    int lineNumber = 0;

    while (getline(input, rawLine)) {
        ++lineNumber;
        const string line = trim(rawLine);
        if (line.empty() || line[0] == '#') {
            continue;
        }

        const vector<string> fields = splitSemicolonLine(line);
        if (fields.size() < 3 || fields.size() > 5) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) +
                                " expected 3 to 5 fields separated by ';'");
        }
        if (fields[0].empty()) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) + " process label cannot be empty");
        }

        Process process{};
        process.id = fields[0];
        process.burst = parseIntField(fields[1], "burst", filePath, lineNumber);
        process.arrival = parseIntField(fields[2], "arrival", filePath, lineNumber);
        process.queue = fields.size() >= 4 ? parseIntField(fields[3], "queue", filePath, lineNumber) : 0;
        process.priority = fields.size() >= 5 ? parseIntField(fields[4], "priority", filePath, lineNumber) : 0;
        process.remaining = process.burst;
        process.inputOrder = static_cast<int>(processes.size());

        if (process.burst <= 0) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) + " burst must be greater than 0");
        }
        if (process.arrival < 0) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) + " arrival must be greater than or equal to 0");
        }
        if (process.queue < 0) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) + " queue must be greater than or equal to 0");
        }
        if (process.priority < 0) {
            throw runtime_error(filePath + ":" + to_string(lineNumber) + " priority must be greater than or equal to 0");
        }

        processes.push_back(process);
    }

    if (processes.empty()) {
        throw runtime_error("No valid processes found in file: " + filePath);
    }

    return processes;
}

bool compareByArrival(const Process& a, const Process& b) {
    if (a.arrival != b.arrival) {
        return a.arrival < b.arrival;
    }
    if (a.queue != b.queue) {
        return a.queue < b.queue;
    }
    if (a.priority != b.priority) {
        return a.priority < b.priority;
    }
    return a.inputOrder < b.inputOrder;
}

void printMetrics(const Metrics& metrics) {
    cout << fixed << setprecision(2);
    cout << "Turnaround avg: " << metrics.turnaroundAvg << '\n';
    cout << "Waiting avg: " << metrics.waitingAvg << '\n';
    cout.unsetf(ios::floatfield);
    cout << setprecision(6);
}

Metrics fcfs(vector<Process> p) {
    sort(p.begin(), p.end(), compareByArrival);
    int time = 0;
    long long totalTurnaround = 0;
    long long totalWaiting = 0;

    cout << "FCFS:\n";

    for (auto& proc : p) {
        if (time < proc.arrival) {
            time = proc.arrival;
        }
        const int start = time;
        const int finish = time + proc.burst;
        cout << proc.id << "  Desde: " << start << "  Hasta: " << finish << '\n';
        totalTurnaround += finish - proc.arrival;
        totalWaiting += start - proc.arrival;
        time = finish;
    }

    return {
        static_cast<double>(totalTurnaround) / p.size(),
        static_cast<double>(totalWaiting) / p.size()
    };
}

bool isBetterSjfCandidate(const Process& candidate, const Process& current) {
    if (candidate.burst != current.burst) {
        return candidate.burst < current.burst;
    }
    if (candidate.arrival != current.arrival) {
        return candidate.arrival < current.arrival;
    }
    if (candidate.queue != current.queue) {
        return candidate.queue < current.queue;
    }
    if (candidate.priority != current.priority) {
        return candidate.priority < current.priority;
    }
    return candidate.inputOrder < current.inputOrder;
}

Metrics sjf(vector<Process> processes) {
    const int n = static_cast<int>(processes.size());
    int completed = 0;
    int time = 0;
    long long totalTurnaround = 0;
    long long totalWaiting = 0;
    vector<bool> done(n, false);

    cout << "\nSJF:\n";

    while (completed < n) {
        int idx = -1;
        for (int i = 0; i < n; ++i) {
            if (done[i] || processes[i].arrival > time) {
                continue;
            }
            if (idx == -1 || isBetterSjfCandidate(processes[i], processes[idx])) {
                idx = i;
            }
        }
        if (idx == -1) {
            ++time;
            continue;
        }

        const int start = time;
        const int finish = time + processes[idx].burst;
        cout << processes[idx].id << "  Desde: " << start << "  Hasta: " << finish << '\n';
        totalTurnaround += finish - processes[idx].arrival;
        totalWaiting += start - processes[idx].arrival;
        time = finish;
        done[idx] = true;
        ++completed;
    }

    return {
        static_cast<double>(totalTurnaround) / n,
        static_cast<double>(totalWaiting) / n
    };
}

bool isBetterStcfCandidate(const Process& candidate, const Process& current) {
    if (candidate.remaining != current.remaining) {
        return candidate.remaining < current.remaining;
    }
    if (candidate.arrival != current.arrival) {
        return candidate.arrival < current.arrival;
    }
    if (candidate.queue != current.queue) {
        return candidate.queue < current.queue;
    }
    if (candidate.priority != current.priority) {
        return candidate.priority < current.priority;
    }
    return candidate.inputOrder < current.inputOrder;
}

Metrics stcf(vector<Process> p) {
    const int n = static_cast<int>(p.size());
    int time = 0;
    int completed = 0;
    int currentIdx = -1;
    int segmentStart = -1;
    vector<int> completionTimes(n, -1);

    for (auto& proc : p) {
        proc.remaining = proc.burst;
    }

    cout << "\nSTCF:\n";

    while (completed < n) {
        int idx = -1;
        for (int i = 0; i < n; ++i) {
            if (p[i].arrival > time || p[i].remaining <= 0) {
                continue;
            }
            if (idx == -1 || isBetterStcfCandidate(p[i], p[idx])) {
                idx = i;
            }
        }

        if (idx == -1) {
            if (currentIdx != -1) {
                cout << p[currentIdx].id << "  Desde: " << segmentStart << "  Hasta: " << time << '\n';
                currentIdx = -1;
                segmentStart = -1;
            }
            ++time;
            continue;
        }

        if (currentIdx != idx) {
            if (currentIdx != -1) {
                cout << p[currentIdx].id << "  Desde: " << segmentStart << "  Hasta: " << time << '\n';
            }
            currentIdx = idx;
            segmentStart = time;
        }

        --p[idx].remaining;
        ++time;

        if (p[idx].remaining == 0) {
            completionTimes[idx] = time;
            ++completed;
        }
    }

    if (currentIdx != -1) {
        cout << p[currentIdx].id << "  Desde: " << segmentStart << "  Hasta: " << time << '\n';
    }

    long long totalTurnaround = 0;
    long long totalWaiting = 0;
    for (int i = 0; i < n; ++i) {
        const int turnaround = completionTimes[i] - p[i].arrival;
        totalTurnaround += turnaround;
        totalWaiting += turnaround - p[i].burst;
    }

    return {
        static_cast<double>(totalTurnaround) / n,
        static_cast<double>(totalWaiting) / n
    };
}

void enqueueArrivals(const vector<Process>& p, vector<bool>& added, queue<int>& q, int time) {
    for (int i = 0; i < static_cast<int>(p.size()); ++i) {
        if (!added[i] && p[i].arrival <= time) {
            q.push(i);
            added[i] = true;
        }
    }
}

Metrics roundRobin(vector<Process> p, int quantum) {
    queue<int> q;
    int time = 0;
    const int n = static_cast<int>(p.size());
    vector<bool> added(n, false);
    vector<int> completionTimes(n, -1);

    sort(p.begin(), p.end(), compareByArrival);

    for (auto& proc : p) {
        proc.remaining = proc.burst;
    }

    cout << "\nRound Robin (Quantum: " << quantum << "):\n";

    while (true) {
        enqueueArrivals(p, added, q, time);

        if (q.empty()) {
            bool done = true;
            for (const auto& proc : p) {
                if (proc.remaining > 0) {
                    done = false;
                    break;
                }
            }
            if (done) {
                break;
            }
            ++time;
            continue;
        }

        const int idx = q.front();
        q.pop();
        const int start = time;
        const int exec = min(quantum, p[idx].remaining);
        const int finish = time + exec;

        cout << p[idx].id << "  Desde: " << start << "  Hasta: " << finish << '\n';

        time = finish;
        p[idx].remaining -= exec;

        enqueueArrivals(p, added, q, time);

        if (p[idx].remaining > 0) {
            q.push(idx);
        } else {
            completionTimes[idx] = time;
        }
    }

    long long totalTurnaround = 0;
    long long totalWaiting = 0;
    for (int i = 0; i < n; ++i) {
        const int turnaround = completionTimes[i] - p[i].arrival;
        totalTurnaround += turnaround;
        totalWaiting += turnaround - p[i].burst;
    }

    return {
        static_cast<double>(totalTurnaround) / n,
        static_cast<double>(totalWaiting) / n
    };
}

void printUsage(const string& programName) {
    cout << "Usage: " << programName << " <input_file> [--verbose|-v] [-q N|--quantum N]\n";
    cout << "Examples:\n";
    cout << "  " << programName << " input_example1.txt\n";
    cout << "  " << programName << " input_example2.txt --verbose\n";
    cout << "  " << programName << " -q 4 input_example3.txt\n";
}

int main(int argc, char* argv[]) {
    try {
        if (argc < 2) {
            printUsage(argv[0]);
            return 1;
        }

        bool verbose = false;
        int quantum = 3;
        string inputFile;

        for (int i = 1; i < argc; ++i) {
            const string arg = argv[i];

            if (arg == "--help") {
                printUsage(argv[0]);
                return 0;
            }
            if (arg == "--verbose" || arg == "-v") {
                verbose = true;
                continue;
            }
            if (arg == "--quantum" || arg == "-q") {
                if (i + 1 >= argc) {
                    throw runtime_error("Missing value for quantum option");
                }
                quantum = parseIntField(argv[++i], "quantum", "CLI", 0);
                if (quantum <= 0) {
                    throw runtime_error("Quantum must be greater than 0");
                }
                continue;
            }
            if (!arg.empty() && arg[0] == '-') {
                throw runtime_error("Unknown option: " + arg);
            }
            if (!inputFile.empty()) {
                throw runtime_error("Only one input file is supported");
            }
            inputFile = arg;
        }

        if (inputFile.empty()) {
            printUsage(argv[0]);
            return 1;
        }

        const vector<Process> processes = loadProcessesFromFile(inputFile);

        if (verbose) {
            cout << "Archivo: " << inputFile << '\n';
            cout << "Procesos cargados: " << processes.size() << "\n\n";
        }

        printMetrics(fcfs(processes));
        cout << '\n';
        printMetrics(sjf(processes));
        cout << '\n';
        printMetrics(stcf(processes));
        cout << '\n';
        printMetrics(roundRobin(processes, quantum));

        return 0;
    } catch (const exception& ex) {
        cerr << "Error: " << ex.what() << '\n';
        cerr << "Use --help to see usage.\n";
        return 1;
    }
}
