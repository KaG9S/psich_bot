create table if not exists users(
    id integer unique,
    name text check(name !=  ''),
    un text,
    age integer check(age >= 0 AND age <= 120),
    timereg text no null
);
create table if not exists sessions(
    id integer unique,
    comment text,
    userid integer
);