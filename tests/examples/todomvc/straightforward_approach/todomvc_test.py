from selene.support.conditions import be
from selene.support.conditions import have

from selene.bys import by_link_text
from selene.conditions import exact_text
from selene.tools import ss, s, visit


class TestTodoMVC(object):

    def test_filter_tasks(self):
        visit('https://todomvc4tasj.herokuapp.com/')

        s('#new-todo').should(be.enabled).set_value('a').press_enter()
        s('#new-todo').should(be.enabled).set_value('b').press_enter()
        s('#new-todo').should(be.enabled).set_value('c').press_enter()

        ss("#todo-list>li").should(have.texts('a', 'b', 'c'))

        ss("#todo-list>li").element_by(exact_text('b')).find(".toggle").click()

        s(by_link_text("Active")).click()
        ss("#todo-list>li").filtered_by(be.Visible()).should(have.texts('a', 'c'))

        s(by_link_text("Completed")).click()
        ss("#todo-list>li").filtered_by(be.Visible()).should(have.texts('b'))

