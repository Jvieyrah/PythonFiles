package tech.ada.java.ds.linkedlist;

import java.util.List;

public interface LinkedList<T> {

    void add(T element);
    void addFirst(T element);
    void addLast(T element);
    T getElement(int index);
    T getFirst();
    T getLast();
    boolean isEmpty();
    int size();
    void insert(T element, int index);
    T removeAt(int index);
    T remove(T element);
    List<T> toList();


}
